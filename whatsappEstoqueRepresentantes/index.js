const puppeteer = require('puppeteer');

const now = new Date;

const month = ["January","February","March","April","May","June","July","August","September","October","November","December"];

let name = month[now.getMonth()];

//criando arquivos .png logo após a coleta da pagina na web **/
gold = 'Arquivo 1' /**  + now.getDate()  + name + now.getFullYear()  + now.getHours() + now.getMinutes() **/ + '.png';
veneza = 'Arquivo 2' /**  + now.getDate()  + name + now.getFullYear() + now.getHours() + now.getMinutes() + **/ + '.png';
barcelona = 'Arquivo 3' /**  + now.getDate()  + name + now.getFullYear() + now.getHours() + now.getMinutes() + **/ + '.png';
jaguar = 'Arquivo 4' /**  + now.getDate()  + name + now.getFullYear() + now.getHours() + now.getMinutes() + **/ + '.png';
confort = 'Arquivo 5' /**  + now.getDate()  + name + now.getFullYear() + now.getHours() + now.getMinutes() + **/ + '.png';
veludinho = 'Arquivo 6' /**  + now.getDate()  + name + now.getFullYear() + now.getHours() + now.getMinutes() + **/ + '.png';

// coletando dados da pagina web **//
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('http://94550ac37bb5.sn.mynetname.net:15001/dev/dgb_/prodash/estoque_pronta_entrega_gold.php');// Acessando pagina web para coleta dos dados **//
  await page.screenshot({ path: '../../../capturaDeTelas/' + gold, fullPage:true }); // tirando screenshot com escala fullpage **/ -  // '../../capturaDeTelas/' + setando pastas para salvar screenshots **/
  await page.goto('http://94550ac37bb5.sn.mynetname.net:15001/dev/dgb_/prodash/estoque_pronta_entrega_veneza.php');
  await page.screenshot({ path: '../../../capturaDeTelas/' + veneza, fullPage:true });
  await page.goto('http://94550ac37bb5.sn.mynetname.net:15001/dev/dgb_/prodash/estoque_pronta_entrega_barcelona.php');
  await page.screenshot({ path: '../../../capturaDeTelas/' + barcelona, fullPage:true });
  await page.goto('http://94550ac37bb5.sn.mynetname.net:15001/dev/dgb_/prodash/estoque_pronta_entrega_jaguar.php');
  await page.screenshot({ path: '../../../capturaDeTelas/' + jaguar, fullPage:true });
  await page.goto('http://94550ac37bb5.sn.mynetname.net:15001/dev/dgb_/prodash/estoque_pronta_entrega_confort.php');
  await page.screenshot({ path: '../../../capturaDeTelas/' + confort, fullPage:true });
  await page.goto('http://94550ac37bb5.sn.mynetname.net:15001/dev/dgb_/prodash/estoque_pronta_entrega_veludinho.php');
  await page.screenshot({ path: '../../../capturaDeTelas/' + veludinho, fullPage:true });
  var dataAtual = new Date();
  //console.log(dataAtual);
  //console.log(name);

  await browser.close();
})();