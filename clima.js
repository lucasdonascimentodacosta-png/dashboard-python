fetch("/clima")
  .then(res => res.json())
  .then(data => {
    document.getElementById("clima").innerText =
      `${data.temp}°C - ${data.desc}`;
  });
