function onClickEstimateDiabetes(){
  var datos = $("#valida_datos").serialize();
  console.log(datos);
  $.ajax({
    type: 'POST',
    url: '/predicted_diabetes',
    data: datos
  }).done(function(response) 
   {	
     var result = document.getElementById('resultado');
     var porcentaje = response['estimated_diabetes'];
     if(response['estimated_diabetes']<50){
      result.innerHTML = "<h2 class='text-info'> You have a " + porcentaje+ "% chance of having diabetes</h2>";
     }else{
      result.innerHTML = "<h2 class='text-danger'> You have a " + porcentaje+ "% chance of having diabetes</h2>";
     } 
   }
 ).fail(function()
   {
     alert("Oops intentalo de nuevo");     
   }
  );
}