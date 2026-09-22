import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav style={{ padding: "1rem", background: "#1a1a2e", color: "#fff" }}>
      <Link to="/" style={{ color: "#fff", marginRight: "1.5rem", textDecoration: "none" }}>
        Home
      </Link>
      <Link to="/dashboard" style={{ color: "#fff", textDecoration: "none" }}>
        Dashboard
      </Link>
    </nav>
  );
}

export default Navbar;