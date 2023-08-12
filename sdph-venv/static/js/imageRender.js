const input = document.getElementById("inputImage");
const imageContainer = document.getElementById("viewImage");

input.addEventListener("change", () => {
  const file = input.files[0];

  if (file) {
    const reader = new FileReader();

    reader.onload = (e) => {
      const img = document.createElement("img");
      img.src = e.target.result;
      img.classList.add("uploaded-image");
      imageContainer.innerHTML = "";
      imageContainer.appendChild(img);
    };

    reader.readAsDataURL(file);
  }
});
