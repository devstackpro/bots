const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: false});
  const page = await browser.newPage();
  await page.goto('https://www.instagram.com/segredosdasvendas');

  await page.evaluate(() => {
      // função executada no browser
      //capturando as imagens
      const nodeList = document.querySelectorAll ('article img')
      //transformar nodelist em array
      const imgArray = [...nodeList]

      // transformar os nodes (elementos html) em objetos js
      const list = imgArray.map ( ({src}) => ({
          src
      }))

      console.log(list)
      //coloca para fora da função
  });
  
  await browser.close();
})();