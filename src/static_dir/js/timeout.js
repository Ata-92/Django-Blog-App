const alerts = document.querySelectorAll(".alert")
setTimeout(() => {
  for (let i = 0; i < alerts.length; i++) {
    alerts[i].style.display = "none"
  }
}, 3000);
