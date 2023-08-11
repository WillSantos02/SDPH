const input = document.getElementById("inputImage");
const viewImageDiv = document.getElementById("viewImage");

input.addEventListener("change", () => {
  const file = input.files[0];

  if (file) {
    const reader = new FileReader();

    reader.onload = (e) => {
      const img = document.createElement("img");
      img.src = e.target.result;
      img.style.maxWidth = "100%";
      img.style.height = "auto";
      viewImageDiv.innerHTML = "";
      viewImageDiv.appendChild(img);
    };

    reader.readAsDataURL(file);
  }
});
