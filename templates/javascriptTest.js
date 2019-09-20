// データ表示
function get_func(url) {
  fetch(url)
  .then(function(response) {
    return response.text();
  })
  .then(function(text) {     // 結果をGetする（コールバック）
    let view = document.getElementById("view")
    view.textContent = ""
    text.split("\n").forEach((value) => {
      view.insertAdjacentHTML('beforeend', value);
      view.insertAdjacentHTML('beforeend', "<br>");
    })
    playSound();
  });
}

// データ追加
function post_func(url) {
  // Postで送る
  let formData = new FormData();
  formData.append('param', document.getElementById('post_param').value);
  fetch(url, {
    method: 'POST',         // methodを指定しないとGETになる
    body: formData,         // Postで送るパラメータを指定
  })
  .then(function() {        // 結果をGetする（コールバック）
    var url2 = url.match(/^https?:\/{2,}(.*?)(?:\/|\?|#|$)/)[1];
    get_func('http://' + url2 + '/get');
    playSound();
  });
}

// データ削除
function del_func(url) {
  fetch(url, {
    method: 'GET',
  })
  .then(function() {        // 結果をGetする（コールバック）
    var url2 = url.match(/^https?:\/{2,}(.*?)(?:\/|\?|#|$)/)[1];
    get_func('http://' + url2 + '/get');
    playSound();
  });
}

var synth;
window.onload = function(){
  synth = new Tone.Synth().toMaster();
}

function playSound() {
  var array = ["C4" ,"C#4","D4" ,"D#4","E4" ,"F4" ,"F#4","G4" ,"G#4","A4" ,"A#4","B4" ,"C5" ];
  synth.triggerAttackRelease(array[Math.floor(Math.random() * array.length)], "8n");
}