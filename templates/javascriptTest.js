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


function playSound() {
    // メロディを鳴らす音源
    var synth = new Tone.Synth().toMaster();
    // メロディの音階データ
    var melody_data = [
      'E5', 'C5', 'G4', 'C5', 'D5', 'G5', null, 'G4',
      'D5', 'E5', 'D5', 'G4', 'C5', null, null, null // nullは休符
    ];
    function addMelody(time, note) {
      synth.triggerAttackRelease(note, '8n', time);
    }
    var melody = new Tone.Sequence(addMelody, melody_data).start();
    // テンポを指定
    Tone.Transport.bpm.value = 140

    Tone.Transport.start();
}