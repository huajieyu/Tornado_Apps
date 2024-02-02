function reset_status(clicked_id){
       var clicked_element = document.getElementById(clicked_id);

       var text_element = clicked_element.textContent || clicked_element.innerText;
       message = text_element;
       // reset the clicked button's background color into #color[0] ffbf00
       // reset the non-clicked button's background color into #color[1] : 04AA6D
       console.log("Chose to reset  the status into", message)

       
}
