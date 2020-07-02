function show(item) {
  var xhttp = new XMLHttpRequest();
  var show = item.id;
  
    xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      
    }
  };
  
  xhttp.open("POST", "/show", true);
  xhttp.setRequestHeader("Content-Type", "application/json")
  xhttp.send(JSON.stringify({"show": show}));
}