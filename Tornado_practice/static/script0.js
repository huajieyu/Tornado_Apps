    // created by L. Jiang (email: libo.jiang@intelsat.com)
    // date: 01/23
    // function of this script: add the event of click on the site names
    
    // #1 define a message 
    let message= "NONE";
    //# change the text in h2
    // #2 display the message in h2
    const titleEl = document.getElementsByClassName("title")[0];
    titleEl.innerHTML = message;
    
    // set up the functions for the reply of the click ================================
    function reply_click(clicked_id)
    {
       // get your element
       
       var clicked_element = document.getElementById(clicked_id);

       var text_element = clicked_element.textContent || clicked_element.innerText;
       message = text_element;
       titleEl.innerHTML = message;

       document.getElementById("selsiteid").value = message; 


       // reset the clicked button's background color into #color[0] ffbf00
       // reset the non-clicked button's background color into #color[1] : 04AA6D
       document.getElementById(clicked_id).style.backgroundColor='#6495ED'; 
       var btnidarray = ['btnand', 'btnatl', 'btnble', 'btnbrw', 'btncrk', 'btnfil', 'btnfoc', 'btnfus', 'btnhbk', 'btnksn', 'btnmgw', 'btnmtn', 'btnnap', 'btnpam', 'btnreg', 'btnrvs', 'btnswf', 'btntos', 'btntest1', 'btntest2'];
       var arrayLength = btnidarray.length;
       for (var i=0; i < arrayLength; i++){
           if (btnidarray[i] != clicked_id) {
                document.getElementById(btnidarray[i]).style.backgroundColor='#CCCCFF';
           }
       }


       console.log("Button was Clicked"); 
    }
    //================================================================================== 
    // #3 click the button to change the text message
    //const btnEl = document.getElementsByClassName("btn")[0]
    const btnEl = document.getElementsByClassName("resetbtn")[0];
    btnEl.addEventListener("click", e => {
      message = "NONE";
      titleEl.innerHTML = message;

      document.getElementById("selsiteid").value = message;

      var btnidarray = ['btnand', 'btnatl', 'btnble', 'btnbrw', 'btncrk', 'btnfil', 'btnfoc', 'btnfus', 'btnhbk', 'btnksn', 'btnmgw', 'btnmtn', 'btnnap', 'btnpam', 'btnreg', 'btnrvs', 'btnswf', 'btntos', 'btntest1', 'btntest2'];
      var arrayLength = btnidarray.length;
      for (var i=0; i < arrayLength; i++){
                document.getElementById(btnidarray[i]).style.backgroundColor='#CCCCFF';
      }
      console.log("Button was Clicked");
    })
    //======================================================================================
    function getDictInfo(clicked_value){
        var genvarDict=jQuery.parseJSON("{{genvarDict}}");
        var subInfo;
        subInfo = [];
        subInfo.push(genvarDict);
        console.log("get all the genvarDict information in myFunction");    
    }


    //=======================================================================================                 
