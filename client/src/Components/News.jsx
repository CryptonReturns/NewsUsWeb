import React from "react";
import { Card, CardTitle, CardText, Row, Col } from "reactstrap";
import { Link } from "react-router-dom";

function NewsCard(props) {
  const { data } = props;
  return (
    <Row>
      <Col
        sm={{ size: 10, offset: 1 }}
        style={{ marginTop: "10px", marginBottom: "10px" }}
      >
        <Card body>
          <Row>
            <Col sm="12">
              <CardTitle>{data.headline}</CardTitle>
            </Col>
          </Row>
          <Row>
            <Col sm="12">
              <CardText>{data.body}</CardText>
            </Col>
          </Row>
          <Row>
            <Col sm="3">
              <CardText style={{ text: "grey" }}>{data.time}</CardText>
            </Col>
            <Col sm="3">
              <CardText>{data.source}</CardText>
            </Col>

            <Col sm={{ size: 3, offset: 3 }}>
              <a href={data.url}>See full article</a>
            </Col>
          </Row>
        </Card>
      </Col>
    </Row>
  );
}

function News(props) {
  let category = "";
  if (props.type === 1) {
    category = "General";
  } else if (props.type === 2) {
    category = "Technology";
  } else if (props.type === 3) {
    category = "Finance";
  } else if (props.type === 4) {
    category = "Sports";
  } else if (props.type === 6) {
    category = "Entertainment";
  } else if (props.type === 5) {
    category = "International";
  }
  console.log(props);
  const x = props.data.map((news) => {
    // if (news.category === category) return <NewsCard data={news} />;
    // else return <></>;
    if (news.headline) {
      return <NewsCard data={news} />;
    } else {
      return <></>;
    }
  });

  return <div>{x}</div>;
}
export default News;
