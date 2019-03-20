var $container = $('.container');
var $backdrop = $('.backdrop');
var $highlights = $('.highlights');
var $textarea = $('textarea');
var $toggle = $('button');
//var symptomps = ['swelling','painkiller','pain','swelling', 'vomiting','muscle paralysis','death'];

function handleInput() {
  var text = $textarea.val();
  var highlightedText = applyHighlights(text);
  //$highlights.html(highlightedText);
}

function bindEvents() {
  $textarea.on({
    'input': handleInput,
    'scroll': handleScroll
  });

  $toggle.on('click', function() {
    $container.toggleClass('perspective');
  });  
}

bindEvents();
handleInput();
function appendScript(src, callback) {
  var head = document.getElementsByTagName('head')[0];

  if (src.endsWith(".js")) {
    var elt = document.createElement("script");
    elt.type = "text/javascript";
    elt.src = src;
  } else {
    var elt = document.createElement("link");
    elt.rel = "stylesheet";
    elt.link = src;
  }

  elt.onload = function() {
    callback();
  }

  head.appendChild(elt);
}

function runTest() {
  $('#aes-text').highlightTextarea({
      words: symptomps,
      id: 'aes-wrap',
      debug: false
  });
    $('#aes-text').highlightTextarea({
      words: brandlist,
      id: 'aes-wrap2',
      debug: false
  });
}





window.onload = runTest;
