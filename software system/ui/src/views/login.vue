<template>
  <div class="login">
    <el-form ref="loginForm"
             :model="loginForm"
             :rules="loginRules"
             class="login-form">
      <h3 class="title">
        欢迎使用地表数据挖掘关联共享工具集
      </h3>
      <el-form-item prop="username">
        <el-input v-model="loginForm.username"
                  type="text"
                  auto-complete="off"
                  placeholder="账号">
          <svg-icon slot="prefix"
                    icon-class="user"
                    class="el-input__icon input-icon" />
        </el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input v-model="loginForm.password"
                  type="password"
                  auto-complete="off"
                  placeholder="密码"
                  @keyup.enter.native="handleLogin">
          <svg-icon slot="prefix"
                    icon-class="password"
                    class="el-input__icon input-icon" />
        </el-input>
      </el-form-item>
      <el-form-item prop="code"
                    v-if="captchaEnabled">
        <el-input v-model="loginForm.code"
                  auto-complete="off"
                  placeholder="验证码"
                  style="width: 63%"
                  @keyup.enter.native="handleLogin">
          <svg-icon slot="prefix"
                    icon-class="validCode"
                    class="el-input__icon input-icon" />
        </el-input>
        <div class="login-code">
          <img :src="codeUrl"
               @click="getCode"
               class="login-code-img" />
        </div>
      </el-form-item>
      <el-checkbox v-model="loginForm.rememberMe"
                   style="margin:0px 0px 25px 0px;">
        记住密码
      </el-checkbox>
      <el-form-item style="width:100%;">
        <el-button :loading="loading"
                   size="medium"
                   type="primary"
                   style="width:50%; "
                   @click.native.prevent="handleLogin">
          <span v-if="!loading">登 录</span>
          <span v-else>登 录 中...</span>
        </el-button>
        <div style="float: right;">
          <router-link class="link-type"
                       :to="'/register'">立即注册</router-link>
        </div>
      </el-form-item>
    </el-form>
    <!-- 底部 -->
    <div class="el-login-footer">
      <span>
        Copyright © 2022-2026 中国地质大学（武汉）计算机学院.
      </span>
    </div>
  </div>
</template>
  
<script>
import { getCodeImg } from "@/api/login";
import { decrypt, encrypt } from "@/utils/jsencrypt";
import Cookies from "js-cookie";

export default {
  name: "Login",
  data () {
    return {
      codeUrl: "",
      loginForm: {
        username: "admin",
        password: "admin123",
        rememberMe: false,
        code: "",
        uuid: "",
      },
      loginRules: {
        username: [
          { required: true, trigger: "blur", message: "请输入您的账号" },
        ],
        password: [
          { required: true, trigger: "blur", message: "请输入您的密码" },
        ],
        code: [{ required: true, trigger: "change", message: "请输入验证码" }],
      },
      loading: false,
      // 验证码开关
      captchaEnabled: true,
      // 注册开关
      register: false,
      redirect: undefined,
    };
  },
  watch: {
    $route: {
      handler: function (route) {
        this.redirect = route.query && route.query.redirect;
      },
      immediate: true,
    },
  },
  created () {
    this.getCode();
    this.getCookie();
  },
  methods: {
    getCode () {
      getCodeImg().then((res) => {
        this.captchaEnabled =
          res.captchaEnabled === undefined ? true : res.captchaEnabled;
        if (this.captchaEnabled) {
          this.codeUrl = "data:image/gif;base64," + res.img;
          this.loginForm.uuid = res.uuid;
        }
      });
    },
    getCookie () {
      const username = Cookies.get("username");
      const password = Cookies.get("password");
      const rememberMe = Cookies.get("rememberMe");
      this.loginForm = {
        username:
          username === undefined ? this.loginForm.username : username,
        password:
          password === undefined ? this.loginForm.password : decrypt(password),
        rememberMe: rememberMe === undefined ? false : Boolean(rememberMe),
      };
    },
    handleLogin () {
      this.$refs.loginForm.validate((valid) => {
        if (valid) {
          this.loading = true;
          if (this.loginForm.rememberMe) {
            Cookies.set("username", this.loginForm.username);
            Cookies.set("password", encrypt(this.loginForm.password));
            Cookies.set("rememberMe", this.loginForm.rememberMe);
          } else {
            Cookies.remove("username");
            Cookies.remove("password");
            Cookies.remove("rememberMe");
          }
          this.$store
            .dispatch("Login", this.loginForm)
            .then(() => {
              this.loading = false;
              this.$router.push({ path: "/dataMap" });
            })
            .catch((err) => {
              this.loading = false;
              this.getCode();
            });
        } else {
          return false;
        }
      });
    },
  },
};
</script>
  
<style scoped>
.login {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  height: 100%;
  background-color: #f0f2f5;
  background-image: url('../assets/images/back1.jpg');
}

.login-form {
  background-color: white;
  padding: 40px 60px;
  width: 450px;
  border-radius: 30px;
}

.title {
  text-align: center;
  margin-bottom: 30px;
  color: blue;
  /*设置文字颜色*/
  text-shadow: 0 8px 10px #6699ff;
  /*设置文字阴影*/
  font-weight: bolder;
  font-family: 'Montserrat', cursive;
  /*设置文字宽度*/
  font-size: 24px;
}

.input-icon {
  fill: #c0c4cc;
  width: 18px;
  height: 18px;
}

.login-code {
  display: inline-block;
  width: 110px;
  height: 36px;
  vertical-align: middle;
  margin-left: 10px;
}

.login-code-img {
  width: 100%;
  height: 100%;
  cursor: pointer;
}

.link-type {
  color: #409eff;
  cursor: pointer;
}

.el-login-footer {
  margin-top: 150px;
  color: white;
  font-size: 17px;
  text-align: center;
  bottom: 0px;
}
</style>