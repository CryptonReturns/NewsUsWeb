import React, { useState } from 'react';
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink
} from 'reactstrap';
import { BrowserRouter as Router , Switch, Route } from 'react-router-dom';
const Example = (props) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => setIsOpen(!isOpen);

  return (
    <>
        <Router>
            <Navbar color="dark" dark expand="md">
                <NavbarBrand href="/">NewsUs</NavbarBrand>
                <NavbarToggler onClick={toggle} />
                <Collapse isOpen={isOpen} navbar>
                <Nav className="mr-auto" navbar>
                    <NavItem>
                        <NavLink href="/categories">Categories</NavLink>
                    </NavItem>
                    <NavItem>
                        <NavLink href="/topHeadlines">Headlines</NavLink>
                    </NavItem>
                </Nav>
                </Collapse>
            </Navbar>
            <Switch>
                <Route exact path="/">
                    <>oknow</>
                </Route>
                <Route exact path="/categories">
                    <>yes</>
                </Route>
                <Route exact path="/topHeadlines">
                    <>no</>
                </Route>
            </Switch>
        </Router>
    </>
  );
}

export default Example;