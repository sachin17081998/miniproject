

$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.modal').modal();
    $('.carousel').carousel();
    $('.modal').modal();
    $('.materialboxed').materialbox();
    // $('.carousel.carousel-slider').carousel({
    //   fullWidth: true,
    //   indicators: true
    // });

    $('.carousel.carousel-slider').carousel({
      fullWidth: true,
      indicators: true
    }, setTimeout(autoplay, 4500));
   
    function autoplay() {
      $('.carousel').carousel('next');
      setTimeout(autoplay, 4500);
    }
  });
  
// function showresult(){
//   alert("hii")
//   document.getElementById("searchresult").style.display="block";
// }


// function myweb(x) {
//   if (x.matches) { // If media query matches
//     $('.carousel.carousel-slider').carousel({
//       fullWidth: false,
//       indicators: false
//     }, setTimeout(autoplay, 4500));
//   } else {
//     $('.carousel.carousel-slider').carousel({
//       fullWidth: true,
//       indicators: true
//     }, setTimeout(autoplay, 4500));
//   }
// }

// var screen = window.matchMedia("(max-width: 600px)")
// myweb(x) // Call listener function at run time
// x.addListener(myweb)


 function showgal(x){
  nature=document.getElementById("naturegallary");
  food=document.getElementById("foodgallary");
  animals=document.getElementById("animalsgallary");
  marriage=document.getElementById("marriagegallary");
  fashion=document.getElementById("fashiongallary");
  events=document.getElementById("eventsgallary");
  cars=document.getElementById("carsgallary");
  bikes=document.getElementById("bikesgallary");
      
     food.style.display="none";
     fashion.style.display="none";
     nature.style.display="none";
     animals.style.display="none";
     marriage.style.display="none";
     events.style.display="none";
     cars.style.display="none";
     bikes.style.display="none";
  if(x=="food"){
     food.style.display="flex";
     fashion.style.display="none";
     nature.style.display="none";
     animals.style.display="none";
     marriage.style.display="none";
     events.style.display="none";
     cars.style.display="none";
     bikes.style.display="none";
   }
   else if(x=="nature"){
    food.style.display="none";
    fashion.style.display="none";
    nature.style.display="flex";
    animals.style.display="none";
    marriage.style.display="none";
    events.style.display="none";
    cars.style.display="none";
    bikes.style.display="none";
  }
  else if(x=="marriage"){
 
    food.style.display="none";
    fashion.style.display="none";
    nature.style.display="none";
    animals.style.display="none";
    marriage.style.display="flex";
    events.style.display="none";
    cars.style.display="none";
    bikes.style.display="none";}
    else if(x=="animals"){
      food.style.display="none";
      fashion.style.display="none";
      nature.style.display="none";
      animals.style.display="flex";
      marriage.style.display="none";
      events.style.display="none";
      cars.style.display="none";
      bikes.style.display="none";
    }else if(x=="fashion"){
      food.style.display="none";
      fashion.style.display="flex";
      nature.style.display="none";
      animals.style.display="none";
      marriage.style.display="none";
      events.style.display="none";
      cars.style.display="none";
      bikes.style.display="none";
    }else if(x=="cars"){
      food.style.display="none";
      fashion.style.display="none";
      nature.style.display="none";
      animals.style.display="none";
      marriage.style.display="none";
      events.style.display="none";
      cars.style.display="flex";
      bikes.style.display="none";
    }else if(x=="bikes"){
      food.style.display="none";
      fashion.style.display="none";
      nature.style.display="none";
      animals.style.display="none";
      marriage.style.display="none";
      events.style.display="none";
      cars.style.display="none";
      bikes.style.display="flex";
    }else if(x=="events"){
      food.style.display="none";
      fashion.style.display="none";
      nature.style.display="none";
      animals.style.display="none";
      marriage.style.display="none";
      events.style.display="flex";
      cars.style.display="none";
      bikes.style.display="none";
    }
 }