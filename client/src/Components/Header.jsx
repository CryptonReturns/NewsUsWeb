import React from "react";
import { Navbar, NavbarBrand, Col } from "reactstrap";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

const Example = (props) => {
  return (
    <>
      <Router>
        <Navbar color="dark" dark expand="md">
          <Col sm="12" md={{ size: 10, offset: 1 }}>
            <NavbarBrand href="/">NewsUs</NavbarBrand>
          </Col>
        </Navbar>
        <Switch>
          <Route exact path="/">
            {/* <>oknow</> */}
          </Route>
        </Switch>
      </Router>
    </>
  );
};

export default Example;
