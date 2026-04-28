const toggle = document.getElementById("menu-toggle");
const navLinks = document.querySelector(".nav-links");

if (toggle && navLinks) {
  toggle.addEventListener("click", () => {
    navLinks.classList.toggle("active");
  });
}

// Dropdown toggle for mobile
const dropdown = document.querySelector(".dropdown");

if (dropdown) {
  dropdown.addEventListener("click", function () {
    if (window.innerWidth <= 768) {
      this.classList.toggle("active");
    }
  });
}


// job seeker form submission

const jobForm = document.getElementById("jobForm");

if (jobForm) {
  jobForm.addEventListener("submit", async function (e) {
    e.preventDefault();

    const formData = new FormData();

    formData.append("name", document.getElementById("name").value);
    formData.append("email", document.getElementById("email").value);
    formData.append("phone", document.getElementById("phone").value);
    formData.append("role", document.getElementById("role").value);
    formData.append("message", document.getElementById("message").value);

    const fileInput = document.getElementById("resume");
    formData.append("resume", fileInput.files[0]);

    try {
      const response = await fetch("http://127.0.0.1:8000/apply", {
        method: "POST",
        body: formData
      });

      const data = await response.json();

      alert(data.message);
      jobForm.reset();

    } catch (error) {
      alert("Error submitting form");
      console.error(error);
    }
  });
}


const recruiterForm = document.getElementById("recruiterForm");

if (recruiterForm) {
  recruiterForm.addEventListener("submit", async function (e) {
    e.preventDefault();

    const formData = new FormData();

    formData.append("company_name", document.querySelector('input[placeholder="Company Name"]').value);
    formData.append("contact_person", document.querySelector('input[placeholder="Contact Person"]').value);
    formData.append("email", document.querySelector('input[type="email"]').value);
    formData.append("phone", document.querySelector('input[placeholder="Phone Number"]').value);
    formData.append("requirement", document.querySelector('textarea').value);

    try {
      const response = await fetch("http://127.0.0.1:8000/hire", {
        method: "POST",
        body: formData
      });

      const data = await response.json();

      alert(data.message);
      recruiterForm.reset();

    } catch (error) {
      alert("Error submitting request");
      console.error(error);
    }
  });
}