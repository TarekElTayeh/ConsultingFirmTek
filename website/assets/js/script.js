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
  const dropArea = document.getElementById("drop-area");
  const fileInput = document.getElementById("file");

  // Highlight drop area when file is dragged over
  dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.classList.add("highlight");
  });

  dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("highlight");
  });

  // Handle file drop
  dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    dropArea.classList.remove("highlight");

    const files = e.dataTransfer.files;
    handleFiles(files);
  });

  // Open file browser on click
  document.getElementById("file-select").addEventListener("click", () => {
    fileInput.click();
  });

  // Handle file selection
  fileInput.addEventListener("change", () => {
    const files = fileInput.files;
    handleFiles(files);
  });

  function handleFiles(files) {
    // Here, you can display selected files or perform additional validation
    console.log("Files selected:", files);
  }
});



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

  document.addEventListener("DOMContentLoaded", () => {
    const typewriter = document.getElementById("typewriter");
    const textArray = ["Empowering Businesses", "Creating Innovative Solutions", "Transforming Ideas Into Reality"];
    let textIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
  
    function type() {
      const currentText = textArray[textIndex];
      typewriter.textContent = currentText.substring(0, charIndex);
  
      if (!isDeleting && charIndex < currentText.length) {
        charIndex++;
        setTimeout(type, 100);
      } else if (isDeleting && charIndex > 0) {
        charIndex--;
        setTimeout(type, 50);
      } else {
        isDeleting = !isDeleting;
        if (!isDeleting) {
          textIndex = (textIndex + 1) % textArray.length;
        }
        setTimeout(type, 1500);
      }
    }
  
    type();
  });
  let currentTestimonial = 0;
const testimonials = document.querySelectorAll(".testimonial");
const totalTestimonials = testimonials.length;

function showTestimonial(index) {
  testimonials.forEach((testimonial, i) => {
    testimonial.style.display = i === index ? "block" : "none";
  });
}

function nextTestimonial() {
  currentTestimonial = (currentTestimonial + 1) % totalTestimonials;
  showTestimonial(currentTestimonial);
}

document.addEventListener("DOMContentLoaded", () => {
  showTestimonial(currentTestimonial);
  setInterval(nextTestimonial, 5000); // Change testimonial every 5 seconds
});
document.querySelectorAll("section").forEach((section) => {
  const observer = new IntersectionObserver(
    ([entry]) => {
      if (entry.isIntersecting) {
        section.classList.add("visible");
        observer.unobserve(section);
      }
    },
    { threshold: 0.2 }
  );
  observer.observe(section);
});
const carousel = document.querySelector('.testimonial-carousel');
let index = 0;

function showNextTestimonial() {
  index = (index + 1) % carousel.children.length;
  carousel.style.transform = `translateX(-${index * 100}%)`;
}

setInterval(showNextTestimonial, 5000);
