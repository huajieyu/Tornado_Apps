function PollDeviceStatus(){

    String.prototype.unescapeHtml = function () {
        var temp = document.createElement("div");
        temp.innerHTML = this;
        var result = temp.childNodes[0].nodeValue;
        temp.removeChild(temp.firstChild);
        return result;
    }

    console.log("getting the dictionary"); 
    var text = '{{devicestatusDict}}';
    console.log("getting the dictionary2", text); 
    var res = JSON.parse(text.unescapeHtml());
    console.log("getting the dictionary3"); 
 
    //subnetDict obj
    let actdeviceobjlist3 = [];
    let actdevicevaluelist3 = [];
    Object.entries(res).forEach((entry) => {
        const [key, value] = entry;
        console.log(`${key}: ${value}`);
        actdeviceobjlist3.push(key);
        actdevicevaluelist3.push(value);
    });

    var text2 = '{{devicestatusDict2}}';
    var res2 = JSON.parse(text2.unescapeHtml());
    //subnetDict obj
    let actdeviceobjlist2 = [];
    let actdevicevaluelist2 = [];
    Object.entries(res2).forEach((entry) => {
        const [key2, value2] = entry;
        console.log(`${key2}: ${value2}`);
        actdeviceobjlist2.push(key2);
        actdevicevaluelist2.push(value2);
    });

    console.log("start fill out the table content!!!") 
   
  const items0 = [];
  //const tempkey = ['key0', 'key1', 'key2'];
  //const tempval = ['Activated', 'Activated', 'Activated'];
  
  idx = 0;
  while (idx<actdeviceobjlist3.length){
      items0.push({device:actdevicevaluelist3[idx], stat:actdevicevaluelist2[idx], act:'testact'});
      idx=idx+1;
  };
  
  function loadTableData(items) {
    const table = document.getElementById("testBody");
    items.forEach( item => {
      let row = table.insertRow();
      let device = row.insertCell(0);
      device.innerHTML = item.device;
      let stat = row.insertCell(1);
      stat.innerHTML = item.stat;
      let act = row.insertCell(2);
      act.innerHTML = item.act;
    });
  }
  loadTableData(items0);
  //loadTableData([]);
}
