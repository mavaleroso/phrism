import * as React from "react";
import Navbar from "../components/layout/navbar.jsx";
import Banner from "../components/landing_page/home/banner.jsx";

const LandingPage = () => (
  <React.Fragment>
    <div style={{ height: "10000px" }}>
      <Navbar />
      <Banner />
    </div>
  </React.Fragment>
);

export default LandingPage;
