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
    get_func('http://127.0.0.1:4000/get');
  });
}

// データ削除
function del_func(url) {
  fetch(url, {
    method: 'GET',
  })
  .then(function() {        // 結果をGetする（コールバック）
    get_func('http://127.0.0.1:4000/get');
  });
}
