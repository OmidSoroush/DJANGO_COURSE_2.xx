$('h1').click(function() {
  console.log('there was a click')
})

$('li').click(function() {
  console.log('any li was click')
})


$('h1').click(function() {
  $(this).text("I was changed")
})



// Key press

$('input').eq(0).keypress(function() {
  $('h3').toggleClass('turnBlue')
})

$('input').eq(0).keypress(function(event) {
  if(event.which=== 13){
    $('h3').toggleClass('turnBlue')
  }
})


// on()

$('h1').on('dblclick', function() {
  $(this).toggleClass('turnRed')
})

$('input').eq(1).on('click', function() {
  $('.container').slideUp(3000)
})
