var land = [];
for (var i = 1;i <= 400;i++) {
  land.push({id:i})
}
var robot = 23;
var target = 298;
var tembok = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,41,61,81,101,121,141,161,181,201,221,241,261,281,301,321,341,361,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,43,44,63,83,45,85,105,125,125,124,123,107,87,67,143,163,183,142,222,223,224,185,165,166,167,147,169,207,206,246,24,27,49,69,70,109,108,58,57,36,56,98,76,96,75,74,72,54,136,137,114,134,135,92,112,91,31,32,71,131,149,170,154,174,190,127,68,210,307,308,309,310,290,270,250,291,292,293,332,352,350,349,369,347,325,345,365,305,285,284,323,343,322,263,245,247,268,248,283,172,192,212,213,214,252,232,255,275,254,333,334,374,368,176,196,197,159,237,238,297,317,317,318,316,338,358,279,278,356,357,199,179,178,99,139,217,277,313,231,230]
var sudah = [];
var looping;
var pohon = [];

//step

var antrian = [];
var pernah = [];
var antrian_id = 1;
var loc = robot;
var y;
var x;
var q=0;
var langkah = 1;
var ceksudah;
var ceksudahflag = false;
var sudahpernah = false;
var path = [];

function determine_path(){
  var zz;
  var yy;
  var bb;
  var xx=target;;
  var aa = pohon.length - 1;
  
  for ( bb = (aa); bb > 0; bb-- ) {
    if ( pohon[bb].anak == xx ) {
      xx=pohon[bb].ortu;
      path.push(xx);
    }
  }
  for ( yy = 0; yy < path.length; yy++ ){
    land[parseInt(path[yy])-1].state = 'white';
  }
  console.log('result : '+path);
}

function bfs_step(){
  if (parseInt(loc)!=parseInt(target)){
    antrian_id = parseInt(antrian_id) + 1;
    //perulangan
    console.log("step for block : " + loc); 
    if ( !istembok(loc) ){
      tembok.push(parseInt(loc));
      
      // atas
      loc = parseInt(loc);
      y = loc - 20;
      if (!istembok(y)) {
        var tem;
        sudahpernah = false;
        for (tem = 0; tem < pernah.length;tem++) {
          if (parseInt(pernah[tem]) == parseInt(y)) {
            sudahpernah = true;
          }
        }
        if (!sudahpernah) {
          land[parseInt(y)-1].state = 'green';
          antrian.push({id:antrian_id,loc:y});
          antrian_id = parseInt(antrian_id)+1;
          pernah.push(parseInt(y));
          //bikin pohon
          pohon.push({ortu:loc,anak:y});
          if (y == target){
            determine_path();
            process.exit();
          }
        }
      }
      // kiri
      loc = parseInt(loc);
      y = loc-1;
      if (!istembok(y)) {
        var tem;
        sudahpernah=false;
        for (tem = 0; tem < pernah.length; tem++) {
          if (parseInt(pernah[tem]) == parseInt(y)) {
              sudahpernah=true;
          }
        }
        if (!sudahpernah) {
          land[parseInt(y)-1].state = 'green';
          antrian.push({id:antrian_id,loc:y});
          antrian_id = parseInt(antrian_id)+1;
          pernah.push(parseInt(y));
          //bikin pohon
          pohon.push({ortu:loc,anak:y});
          if(y == target){
            determine_path();
            process.exit();
          }
        }
      }
      // bawah
      loc = parseInt(loc);
      y = loc+20;
      if (!istembok(y)) {
        var tem;
        sudahpernah = false;
        for (tem = 0; tem < pernah.length; tem++) {
          if (parseInt(pernah[tem]) == parseInt(y)) {
            sudahpernah = true;
          }
        }
        if (!sudahpernah) {
          land[parseInt(y)-1].state = 'green';
          antrian.push({id:antrian_id,loc:y});
          antrian_id = parseInt(antrian_id)+1;
          pernah.push(parseInt(y));
          //bikin pohon
          pohon.push({ortu:loc,anak:y});
          if(y == target){
              determine_path();
              process.exit();
          }
        }
      }
      // kanan
      loc = parseInt(loc);
      y = loc+1;
      if (!istembok(y)) {
        var tem;
        sudahpernah = false;
        for (tem = 0; tem < pernah.length; tem++) {
          if (parseInt(pernah[tem]) == parseInt(y)) {
            sudahpernah = true;
          }
        }
        if (!sudahpernah) {
          land[parseInt(y)-1].state = 'green';
          antrian.push({id:antrian_id,loc:y});
          antrian_id = parseInt(antrian_id)+1;
          pernah.push(parseInt(y));
          //bikin pohon
          pohon.push({ortu:loc,anak:y});
          if (y == target) {
            determine_path();
            process.exit();
          }
        }
      }
        
      // selesai ambil sekeliling
      if (ceksudahflag) {
        q++;
        ceksudahflag=false;
      }
      q=parseInt(q);
      loc = antrian[q].loc;
      var tem;
      for(tem=0;tem<tembok.length;tem++){
        if(parseInt(tembok[tem])==parseInt(loc)){
          ceksudah = true;
        }
      }
      if(ceksudah){
        loc = parseInt(antrian[q].loc)
        loc = '';
        loc = parseInt(antrian[q].loc)
        ceksudahflag=true;
        land[parseInt(loc)-1].step = langkah;
        land[parseInt(loc)-1].state = 'yellow';
        var loc_ = parseInt(antrian[q].loc)
        langkah++
      } else {
        land[parseInt(loc)-1].step = langkah;
        land[parseInt(loc)-1].state = 'yellow';
        var loc_ = parseInt(antrian[q].loc)
        langkah++
      }
    } 
    q++; 
  }
}

function bfs_loop(){
  while (true) {
    bfs_step();
  }
}

function istembok(id){
    var i;
    for(i=0;i<400; i++){
        if(id==tembok[i]){
            return true;
        }
    }
}
//fungsi gerak
function derajat0(){
  id_now = id_current-1;
  land[parseInt(id_now)].state = 'yellow';
  id_current = id_now; 
}
function derajat90(){
  id_now = id_current-20;
  land[parseInt(id_now)].state = 'yellow';
  id_current = id_now; 
}
function derajat180(){
  id_now = id_current+1;
  land[parseInt(id_now)].state = 'yellow';
  id_current = id_now; 
}
function derajat270(){
  id_now = id_current+20;
  land[parseInt(id_now)].state = 'yellow';
  id_current = id_now; 
}
bfs_loop()
