async function fetchData() {
  try {
    const response = await fetch("http://localhost:8000/data");
    const data = await response.json();

    const tohtml = document.getElementById("dataplace");
    tohtml.innerHTML = json.stringfy(data, ["id", "name", "content"], 2);
  } catch (e) {
    console.log("error fetching... api data", e);
  }
}

window.onload = fetchData;
