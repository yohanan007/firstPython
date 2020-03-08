console.log("ca marche");

 var app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
      isActive: true,
      activeColor: 'red',
      fontSize: 30,
      message: 'vous affichez cette page à :' + new Date().toLocaleString()
    }
  });


  console.log(app);