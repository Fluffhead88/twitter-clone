console.log("Hello World");
/*
let x = fetch('/tweets/').then(function(response) {
  response.json().then(function(data) {
    data.forEach(function(tweet) {
      let container = document.getElementById("tweets");
      let listItem = document.createElement("li"); // <li></li>
      let itemText = document.createTextNode(tweet.body)

      listItem.appendChild(itemText);
      container.appendChild(listItem);
    });
  });
});
*/
function addTweets(data) {
  // debugger;
  // delete all tweets
  let container = document.getElementById("tweets");
  container.innerHTML = "";
  // add all tweets 
  data.forEach(function(tweet) {
    let listItem = document.createElement("li"); // <li></li>
    let itemText = document.createTextNode(tweet.body)

    listItem.appendChild(itemText);
    container.appendChild(listItem);
  });

}

// async/await

async function getData() {
  //debugger;
  let response = await fetch("/tweets/");
  let data = await response.json();
  addTweets(data);

}
let element = document.getElementById("getDataButton");
element.addEventListener("click", getData);