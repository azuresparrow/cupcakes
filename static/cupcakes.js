const BASE_URL = "http://localhost:5000/api";

function cupcakeHTML(cupcake) {
  return `
    <div data-cupcake-id=${cupcake.id}>
        <span class='text-primary'>${cupcake.flavor}</span>  <span class='text-secondary'>${cupcake.size}</span>  <span class="text-muted"> ${cupcake.rating}</span> <button class="btn btn-danger">X</button>
        <img class="cc-img" src="${cupcake.image}"
    </div>
  `;
}

async function showCupcakes() {
  const response = await axios.get(`${BASE_URL}/cupcakes`);

  for (let cupcakeData of response.data.cupcakes) {
    let cupcake = $(cupcakeHTML(cupcakeData));
    $("#cupcakes").append(cupcake);
  }
}

$("#new-cupcake-form").on("submit", async function (e) {
  e.preventDefault();
  let flavor = $("#flavor").val();
  let rating = $("#rating").val();
  let size = $("#size").val();
  let image = $("#image").val();

  const response = await axios.post(`${BASE_URL}/cupcakes`, { flavor, rating, size, image });

  let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
  $("#cupcakes-list").append(newCupcake);
  $("#new-cupcake-form").trigger("reset");
});

$("#cupcakes-list").on("click", ".delete-button", async function (e) {
  e.preventDefault();
  let $cupcake = $(evt.target).closest("div");
  let cupcakeId = $cupcake.attr("data-cupcake-id");
  await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
  $cupcake.remove();
});


$(showCupcakes);