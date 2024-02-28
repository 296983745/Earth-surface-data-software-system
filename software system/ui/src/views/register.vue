<template>
    <div class="register">
        <el-form ref="registerForm" :model="registerForm" :rules="registerRules" class="register-form">
            <h3 class="title">欢迎使用地表数据挖掘关联共享工具集
            </h3>
            <el-form-item prop="username">
                <el-input v-model="registerForm.username" type="text" auto-complete="off" placeholder="账号">
                    <svg-icon slot="prefix" icon-class="user" class="el-input__icon input-icon" />
                </el-input>
            </el-form-item>
            <el-form-item prop="password">
                <el-input v-model="registerForm.password" type="password" auto-complete="off" placeholder="密码"
                    @keyup.enter.native="handleRegister">
                    <svg-icon slot="prefix" icon-class="password" class="el-input__icon input-icon" />
                </el-input>
            </el-form-item>
            <el-form-item prop="confirmPassword">
                <el-input v-model="registerForm.confirmPassword" type="password" auto-complete="off" placeholder="确认密码"
                    @keyup.enter.native="handleRegister">
                    <svg-icon slot="prefix" icon-class="password" class="el-input__icon input-icon" />
                </el-input>
            </el-form-item>
            <el-form-item prop="code" v-if="captchaEnabled">
                <el-input v-model="registerForm.code" auto-complete="off" placeholder="验证码" style="width: 63%"
                    @keyup.enter.native="handleRegister">
                    <svg-icon slot="prefix" icon-class="validCode" class="el-input__icon input-icon" />
                </el-input>
                <div class="register-code">
                    <img :src="codeUrl" @click="getCode" class="register-code-img" />
                </div>
            </el-form-item>
            <el-form-item style="width:100%;">
                <el-button :loading="loading" size="medium" type="primary" style="width:100%;"
                    @click.native.prevent="handleRegister">
                    <span v-if="!loading">注 册</span>
                    <span v-else>注 册 中...</span>
                </el-button>
                <div style="float: right;">
                    <router-link class="link-type" :to="'/login'">使用已有账户登录</router-link>
                </div>
            </el-form-item>
        </el-form>
        <!--  底部  -->
 <div class="el-register-footer">
            <span> Copyright © 2022-2026 中国地质大学（武汉）计算机学院.</span>
        </div>
    </div>
</template>

<script>
import { getCodeImg, register } from "@/api/login";

export default {
    name: "Register",
    data() {
        const equalToPassword = (rule, value, callback) => {
            if (this.registerForm.password !== value) {
                callback(new Error("两次输入的密码不一致"));
            } else {
                callback();
            }
        };
        return {
            codeUrl: "",
            registerForm: {
                username: "",
                password: "",
                confirmPassword: "",
                code: "",
                uuid: ""
            },
            registerRules: {
                username: [
                    { required: true, trigger: "blur", message: "请输入您的账号" },
                    { min: 2, max: 20, message: '用户账号长度必须介于 2 和 20 之间', trigger: 'blur' }
                ],
                password: [
                    { required: true, trigger: "blur", message: "请输入您的密码" },
                    { min: 5, max: 20, message: '用户密码长度必须介于 5 和 20 之间', trigger: 'blur' }
                ],
                confirmPassword: [
                    { required: true, trigger: "blur", message: "请再次输入您的密码" },
                    { required: true, validator: equalToPassword, trigger: "blur" }
                ],
                code: [{ required: true, trigger: "change", message: "请输入验证码" }]
            },
            loading: false,
            captchaEnabled: true
        };
    },
    created() {
        this.getCode();
    },
    methods: {
        getCode() {
            getCodeImg().then(res => {
                this.captchaEnabled = res.captchaEnabled === undefined ? true : res.captchaEnabled;
                if (this.captchaEnabled) {
                    this.codeUrl = "data:image/gif;base64," + res.img;
                    this.registerForm.uuid = res.uuid;
                }
            });
        },
        handleRegister() {
            this.$refs.registerForm.validate(valid => {
                if (valid) {
                    this.loading = true;
                    register(this.registerForm).then(res => {
                        const username = this.registerForm.username;
                        this.$alert("<font color='red'>恭喜你，您的账号 " + username + " 注册成功！</font>", '系统提示', {
                            dangerouslyUseHTMLString: true,
                            type: 'success'
                        }).then(() => {
                            this.$router.push("/login");
                        }).catch(() => { });
                    }).catch(() => {
                        this.loading = false;
                        if (this.captchaEnabled) {
                            this.getCode();
                        }
                    })
                }
            });
        }
    }
};
</script>

<style rel="stylesheet/scss" lang="scss">
.register {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    height: 100%;
    background-color: #f0f2f5;
    background-image: url("../assets/images/back3.png");
}

.register-form {
    background-color: white;
    padding: 40px 60px;
    width: 450px;
}

.title {
    text-align: center;
    margin-bottom: 30px;
    color: blue;
    /*设置文字颜色*/
    text-shadow: 0 8px 10px #6699FF;
    /*设置文字阴影*/
    font-weight: bolder;
    /*设置文字宽度*/
}

.input-icon {
    fill: #c0c4cc;
    width: 18px;
    height: 18px;
}

.register-code {
    display: inline-block;
    width: 100px;
    height: 38px;
    vertical-align: middle;
    margin-left: 10px;
}

.register-code-img {
    width: 100%;
    height: 100%;
    cursor: pointer;
}

.link-type {
    color: #409eff;
    cursor: pointer;
}

.el-register-footer {
    margin-top: 150px;
    color: white;
    font-size: 17px;
    text-align: center;
}
</style>
