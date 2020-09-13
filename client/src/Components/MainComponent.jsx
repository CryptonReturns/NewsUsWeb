import React, { Component } from "react";
import Header from "./Header.jsx";
import "bootstrap/dist/css/bootstrap.css";
import { Col } from "reactstrap";
import TabBar from "./TabBar.jsx";

export default class MainComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isOpen: false,
    };
  }

  render() {
    return (
      <>
        <Header />
        <Col sm="12" md={{ size: 10, offset: 1 }}>
          <TabBar />
        </Col>
      </>
    );
  }
}
