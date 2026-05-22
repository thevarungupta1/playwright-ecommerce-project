function login() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const error = document.getElementById("login-error");

  if (email === "admin@test.com" && password === "Admin@123") {
    localStorage.setItem("user", email);
    window.location.href = "products.html";
  } else {
    error.innerText = "Invalid email or password";
  }
}

function addToCart(productName, price) {
  const cart = JSON.parse(localStorage.getItem("cart") || "[]");
  cart.push({ productName, price });
  localStorage.setItem("cart", JSON.stringify(cart));
  document.getElementById("cart-message").innerText = productName + " added to cart";
}

function loadCart() {
  const cart = JSON.parse(localStorage.getItem("cart") || "[]");
  const cartList = document.getElementById("cart-list");
  const total = document.getElementById("total");

  let totalAmount = 0;
  cartList.innerHTML = "";

  cart.forEach(item => {
    totalAmount += item.price;
    const li = document.createElement("li");
    li.innerText = item.productName + " - ₹" + item.price;
    cartList.appendChild(li);
  });

  total.innerText = "Total: ₹" + totalAmount;
}

function placeOrder() {
  const name = document.getElementById("name").value;
  const address = document.getElementById("address").value;
  const payment = document.getElementById("payment").value;
  const error = document.getElementById("checkout-error");

  if (!name || !address || !payment) {
    error.innerText = "All fields are required";
    return;
  }

  localStorage.removeItem("cart");
  window.location.href = "success.html";
}