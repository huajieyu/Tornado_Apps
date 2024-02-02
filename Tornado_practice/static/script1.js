//<script>
    String.prototype.unescapeHtml = function () {
        var temp = document.createElement("div");
        temp.innerHTML = this;
        var result = temp.childNodes[0].nodeValue;
        temp.removeChild(temp.firstChild);
        return result;
    }

    var text = '{{devicesDict}}';
    var obj = JSON.parse(text.unescapeHtml());


    // console.log(JSON.stringify(obj, null, 2));

    //document.getElementById("demo").innerHTML =
    //    "Selected TTC Site is " +
    //    obj.site_name;
        //obj.site_name + "<br>" +
        //obj.zero + "<br>" +
        //obj.one + "<br>" +
        //obj.two;

    var text = '{{subnetDict}}';
    var res = JSON.parse(text.unescapeHtml());
    //subnetDict obj
    let subnetobjlist = [];
    let subnetvaluelist = [];
    Object.entries(res).forEach((entry) => {
        const [key, value] = entry;
        console.log(`${key}: ${value}`);
        subnetobjlist.push(key);
        subnetvaluelist.push(key);
    });


    var text = '{{crbDict}}';
    var res = JSON.parse(text.unescapeHtml());

    //crbobjlist crbvaluelist
    let crbobjlist  = [];
    let crbvaluelist = [];

    Object.entries(res).forEach((entry) => {
          const [key, value] = entry;
          console.log(`${key}: ${value}`);
        
          crbobjlist.push(key);
          crbvaluelist.push(value);

    });

    
    var text = '{{cortexDict}}';
    var res = JSON.parse(text.unescapeHtml());
    //cortexobjlist, cortexvaluelist 
    let cortexobjlist  = [];
    let cortexvaluelist = [];

    Object.entries(res).forEach((entry) => {
          const [key, value] = entry;
          console.log(`${key}: ${value}`);

          cortexobjlist.push(key);
          cortexvaluelist.push(value);  

    });


    function favTutorial1() {
    var mylist = document.getElementById('myList1');
    let id1 = 0;
    while (id1<crbobjlist.length){
        mylist.add(new Option(subnetobjlist[id1]));
        id1++;
    }
    //document.getElementById("selsubnet").value = mylist.options[mylist.selectedIndex].text;
    }
    function favTutorial2() {
    var mylist = document.getElementById('myList2');
    let id2 = 0;
    while (id2<crbvaluelist.length){
        mylist.add(new Option(crbobjlist[id2]+": "+crbvaluelist[id2]));
        id2++;
    }
    //document.getElementById("selcrb").value = mylist.options[mylist.selectedIndex].text;
    }
    function favTutorial3() {
    var mylist = document.getElementById('myList3');
    let id3 = 0;
    while (id3<cortexvaluelist.length){
        mylist.add(new Option(cortexvaluelist[id3]));
        id3++;
    }
    //document.getElementById("selcortex").value = mylist.options[mylist.selectedIndex].text;
    }
    function populatedropdowns(){
        favTutorial1();
        favTutorial2();
        favTutorial3();
    }
    function onchange_subnet(e){
        var mylist1 = document.getElementById('myList1');
        document.getElementById("selsubnet").value = mylist1.options[mylist1.selectedIndex].text;
        //console.log(e)
    }
    function onchange_crb(e){
        var mylist2 = document.getElementById('myList2');
        document.getElementById("selcrb").value = mylist2.options[mylist2.selectedIndex].text;
        //console.log(e)
    }
    function onchange_cortex(e){
        var mylist3 = document.getElementById('myList3');
        document.getElementById("selcortex").value = mylist3.options[mylist3.selectedIndex].text;
        //console.log(e)
    }

//</script> 


//**************************************************************



//**************************************************************
//<script>
/*    let btnGet = document.querySelector('button');
    let myTable = document.querySelector('#table');


    let employees = [
        { name: 'James', age: 21, country: 'United States'},
        { name: 'Rony', age: 21, country: 'United Kingdom'},
        { name: 'Peter', age: 21, country: 'Canada'},
        { name: 'Marks', age: 21, country: 'Spain'}
    ];

    let headers = ['Subnets', 'Active Devices', 'Crb Number', 'Cortex Number'];

    btnGet.addEventListener('click', () => {
        let table = document.createElement('table');
        let headerRow = document.createElement('tr');
   
        headers.forEach(headerText => {
            let header = document.createElement('th');
            let textNode = document.createTextNode(headerText);
            header.appendChild(textNode);
            headerRow.appendChild(header);
        }); 
        table.appendChild(headerRow);
        myTable.appendChild(table);


    });
//</script>
*/
