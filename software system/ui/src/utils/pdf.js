//pdf.js
import html2Canvas from 'html2canvas';
import jsPDF from 'jspdf';
 
export default {
  install(Vue) {
    // eslint-disable-next-line func-names
    Vue.prototype.getPdf = function (title, ele) {
      const dom = document.querySelector(ele);
      html2Canvas(dom, {
        useCORS: true,//解决网络图片跨域问题
        width: dom.width,
        height: dom.height,
        windowWidth: dom.scrollWidth,
        dpi: window.devicePixelRatio * 4, // 将分辨率提高到特定的DPI 提高四倍
        scale: 4, // 按比例增加分辨率
      }).then((canvas) => {
        // eslint-disable-next-line new-cap
        const pdf = new jsPDF('p', 'mm', 'a4'); // A4纸，纵向
        const ctx = canvas.getContext('2d');
        const a4w = 170; const a4h = 257; // A4大小，210mm x 297mm，四边各保留20mm的边距，显示区域170x257
        const imgHeight = Math.floor(a4h * canvas.width / a4w); // 按A4显示比例换算一页图像的像素高度
        let renderedHeight = 0;
 
        while (renderedHeight < canvas.height) {
          const page = document.createElement('canvas');
          page.width = canvas.width;
          page.height = Math.min(imgHeight, canvas.height - renderedHeight);// 可能内容不足一页
 
          // 用getImageData剪裁指定区域，并画到前面创建的canvas对象中
          page.getContext('2d').putImageData(ctx.getImageData(0, renderedHeight, canvas.width, Math.min(imgHeight, canvas.height - renderedHeight)), 0, 0);
          pdf.addImage(page.toDataURL('image/jpeg', 1.0), 'JPEG', 20, 20, a4w, Math.min(a4h, a4w * page.height / page.width)); // 添加图像到页面，保留10mm边距
 
          renderedHeight += imgHeight;
          if (renderedHeight < canvas.height) {
            pdf.addPage();// 如果后面还有内容，添加一个空页
          }
          // 预览pdf(这里我用的是事件总线把canvas传递过去展示，达到模拟pdf预览的效果，有用但效果不是很好，有需要的可以自行修改)
          //this.$EventBus.$emit('open-pdf', canvas);
        }
        // 保存文件
        pdf.save(`${title}.pdf`);
      });
    };
  },
};