document.addEventListener("DOMContentLoaded", function(){
    // Portfolio section : Load items from JSON
    fetch("assets/data/portfolio.json")
    .then(response => response.json())
    .then(data => {
        const portfolioItems = document.getElementById("porfolio-items");
        data.forEach(item => {
            const itemDiv = document.createElement("div");
            itemDiv.classList.add("portfolio-items");

            const title = document.createElement("h3");
            title.textContent = item.title;

            const description = document.createElement("p");
            description.textContent = item.description;

            itemDiv.appendChild(title);
            itemDiv.appendChild(description)
            portfolioItems.appendChild(itemDiv)
        });
    })
    .catch(error => console.error("Error loading portfolio data:", error));
})


document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
  
    form.addEventListener("submit", function (e) {
      const name = document.getElementById("name");
      const email = document.getElementById("email");
      const message = document.getElementById("message");
  
      if (!name.value || !email.value || !message.value) {
        e.preventDefault(); // Prevent form submission
        alert("Please fill out all fields before submitting the form.");
      }
    });
  });
  