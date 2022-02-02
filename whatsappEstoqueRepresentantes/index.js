const puppeteer = require('puppeteer');

const now = new Date;

const month = ["January","February","March","April","May","June","July","August","September","October","November","December"];

let name = month[now.getMonth()];


gold = 'Arquivo 1' /**  + now.getDate()  + name + now.getFullYear() + now.getHours() + now.getMinutes() + **/ + '.png';
gold2 = 'Arquivo 2' /**  + now.getDate()  + name + now.getFullYear() + now.getHours() + now.getMinutes() + **/ + '.png';
gold3 = 'Arquivo 3' /**  + now.getDate()  + name + now.getFullYear() + now.getHours() + now.getMinutes() + **/ + '.png';

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('http://94550ac37bb5.sn.mynetname.net:15001/dev/dgb_/prodash/estoque_pronta_entrega_gold.php');
  await page.screenshot({ path: gold, fullPage:true });
  await page.goto('http://94550ac37bb5.sn.mynetname.net:15001/dev/dgb_/prodash/estoque_pronta_entrega_gold.php');
  await page.screenshot({ path: gold2, fullPage:true });
  await page.goto('http://94550ac37bb5.sn.mynetname.net:15001/dev/dgb_/prodash/estoque_pronta_entrega_gold.php');
  await page.screenshot({ path: gold3, fullPage:true });
  var dataAtual = new Date();
  //console.log(dataAtual);
  //console.log(name);

  await browser.close();
})();