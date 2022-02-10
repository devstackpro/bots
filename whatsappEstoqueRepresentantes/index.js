const puppeteer = require('puppeteer');

const now = new Date;

var dataAtual = new Date();
  //console.log(dataAtual);
  //console.log(name);

const month = ["January","February","March","April","May","June","July","August","September","October","November","December"];

let name = month[now.getMonth()];

//criando arquivos .png logo após a coleta da pagina na web **/
gold = 'Arquivo_1' /**  + now.getDate()  + name + now.getFullYear()  + now.getHours() + now.getMinutes() **/ + '.png';
veneza = 'Arquivo_2' /**  + now.getDate()  + name + now.getFullYear() + now.getHours() + now.getMinutes() + **/ + '.png';
barcelona = 'Arquivo_3' /**  + now.getDate()  + name + now.getFullYear() + now.getHours() + now.getMinutes() + **/ + '.png';
jaguar = 'Arquivo_4' /**  + now.getDate()  + name + now.getFullYear() + now.getHours() + now.getMinutes() + **/ + '.png';
confort = 'Arquivo_5' /**  + now.getDate()  + name + now.getFullYear() + now.getHours() + now.getMinutes() + **/ + '.png';
veludinho = 'Arquivo_6' /**  + now.getDate()  + name + now.getFullYear() + now.getHours() + now.getMinutes() + **/ + '.png';
contadorScreenshot = 0;
log = '';
success = '';

// coletando dados da pagina web **//
(async () => {
  const browser = await puppeteer.launch({headless: false});
  const page = await browser.newPage();

  try {
    await page.goto('http://94550ac37bb5.sn.mynetname.net:15001/dev/dgb_/prodash/estoque_pronta_entrega_gold.php');// Acessando pagina web para coleta dos dados **//
    await page.screenshot({ path: '../../../capturaDeTelas/' + gold, fullPage:true }); // tirando screenshot com escala fullpage **/ -  // '../../capturaDeTelas/' + setando pastas para salvar screenshots **/
    contadorScreenshot = contadorScreenshot + 1; 
    success = contadorScreenshot; 
  } catch (err) {
      console.log(err);
      log = log + err + ' | ';
      await browser.close()
    }

  
  try {
    await page.goto('http://94550ac37bb5.sn.mynetname.net:15001/dev/dgb_/prodash/estoque_pronta_entrega_veneza.php');
    await page.screenshot({ path: '../../../capturaDeTelas/' + veneza, fullPage:true });
    contadorScreenshot = contadorScreenshot + 1;
    success = contadorScreenshot; 
  } catch (err) {
      console.log(err);
      log = log + err + ' | ';
      await browser.close()
    }


  try {        
    await page.goto('http://94550ac37bb5.sn.mynetname.net:15001/dev/dgb_/prodash/estoque_pronta_entrega_barcelona.php');
    await page.screenshot({ path: '../../../capturaDeTelas/' + barcelona, fullPage:true });
    contadorScreenshot = contadorScreenshot + 1; 
    success = contadorScreenshot; 
  } catch (err) {
      console.log(err);
      log = log + err + ' | ';
      await browser.close()
    }


  try {        
    await page.goto('http://94550ac37bb5.sn.mynetname.net:15001/dev/dgb_/prodash/estoque_pronta_entrega_jaguar.php');
    await page.screenshot({ path: '../../../capturaDeTelas/' + jaguar, fullPage:true });
    contadorScreenshot = contadorScreenshot + 1; 
    success = contadorScreenshot; 
  } catch (err) {
      console.log(err);
      log = log + err + ' | ';
      await browser.close()
    }


  try {      
    await page.goto('http://94550ac37bb5.sn.mynetname.net:15001/dev/dgb_/prodash/estoque_pronta_entrega_confort.php');
    await page.screenshot({ path: '../../../capturaDeTelas/' + confort, fullPage:true });
    contadorScreenshot = contadorScreenshot + 1; 
    success = contadorScreenshot; 
  } catch (err) {
      console.log(err);
      log = log + err + ' | ';
      await browser.close()
    }


  try {       
    await page.goto('http://94550ac37bb5.sn.mynetname.net:15001/dev/dgb_/prodash/estoque_pronta_entrega_veludinho.php');
    await page.screenshot({ path: '../../../capturaDeTelas/' + veludinho, fullPage:true });
    contadorScreenshot = contadorScreenshot + 1; 
    success = contadorScreenshot; 
  } catch (err) {
      console.log(err);
      log = log + err + ' | ';
      await browser.close()
    }


  /** try {       
    await page.goto('http://dgbcomex.com.br');
    await page.screenshot({ path: '../../../capturaDeTelas/' + contadorScreenshot + '.png', fullPage:true });
  } catch (err) {
      console.log(err);
      log = log + err + ' | ';
      await browser.close()
    }**/

    if (log) {
      var fs = require('fs');
      
        fs.writeFile("D://capturaDeTelas//log.txt", now.getDate()  + name + now.getFullYear()  + now.getHours() + now.getMinutes() + log + ' | ', function(erro) {

        if(erro) {
          throw erro;
        }
        console.log("Arquivo salvo");
      });  
    } else{
      var fs = require('fs');
      
        fs.writeFile("D://capturaDeTelas//log.txt", now.getDate()  + name + now.getFullYear()  + now.getHours() + now.getMinutes() + 'success | ', function(erro) {

        if(erro) {
          throw erro;
        }
        console.log("Arquivo salvo");
      });  

    }


  

await browser.close();
})();