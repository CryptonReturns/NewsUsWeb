import React, { useState } from "react";
import { TabContent, TabPane, Nav, NavItem, NavLink } from "reactstrap";
import classnames from "classnames";
import News from "./News";
import content from "../sample";

const TabBar = (props) => {
  const [activeTab, setActiveTab] = useState("1");

  const toggle = (tab) => {
    if (activeTab !== tab) setActiveTab(tab);
  };

  return (
    <div>
      <Nav tabs>
        <NavItem>
          <NavLink
            className={classnames({ active: activeTab === "1" })}
            onClick={() => {
              toggle("1");
            }}
          >
            General
          </NavLink>
        </NavItem>
        {/* <NavItem>
          <NavLink
            className={classnames({ active: activeTab === "2" })}
            onClick={() => {
              toggle("2");
            }}
          >
            Technology
          </NavLink>
        </NavItem> */}
        <NavItem>
          <NavLink
            className={classnames({ active: activeTab === "3" })}
            onClick={() => {
              toggle("3");
            }}
          >
            Finance
          </NavLink>
        </NavItem>
        <NavItem>
          <NavLink
            className={classnames({ active: activeTab === "4" })}
            onClick={() => {
              toggle("4");
            }}
          >
            Sports
          </NavLink>
        </NavItem>
        <NavItem>
          <NavLink
            className={classnames({ active: activeTab === "5" })}
            onClick={() => {
              toggle("5");
            }}
          >
            International
          </NavLink>
        </NavItem>
        <NavItem>
          <NavLink
            className={classnames({ active: activeTab === "6" })}
            onClick={() => {
              toggle("6");
            }}
          >
            Entertainment
          </NavLink>
        </NavItem>
      </Nav>

      <TabContent activeTab={activeTab}>
        <TabPane tabId="1">
          <News type={1} data={content.general} />
        </TabPane>
        {/* <TabPane tabId="2">
          <News type={2} data={content.technology} />
        </TabPane> */}
        <TabPane tabId="3">
          <News type={3} data={content.finance} />
        </TabPane>
        <TabPane tabId="4">
          <News type={4} data={content.sports} />
        </TabPane>
        <TabPane tabId="5">
          <News type={5} data={content.international} />
        </TabPane>
        <TabPane tabId="6">
          <News type={6} data={content.entertainment} />
        </TabPane>
      </TabContent>
    </div>
  );
};

export default TabBar;
