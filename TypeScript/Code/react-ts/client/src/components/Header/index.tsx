import React from "react"
import { Col, Container, Row } from "reactstrap";

export interface IHeaderProps {
  height?: string,
  image?: string,
  title: string,
  headline: string,
}

const Header: React.FunctionComponent<IHeaderProps> = props => {
  const { children, height, image, headline, title } = props;
  const headerStyle = {
    background: "linear-gradient(rgba(36, 20, 38, 0.5), rgba(36, 39, 38, 0.5)), url(" + image + ") no-repeat center center",
    webkitBackgroundSize: "cover",
    MozBackgroundSize: "conver",
    OBackgroundSize: "cover",
    backgroundSize: "cover",
    backgroundRepeat: "no-repeat",
    backgroundPosition: "center",
    width: "100%",
    height: height
  }
  return (
    <header style={headerStyle}>
      <Container>
        <Row className="align-items-center text-center">
          <Col>
            <h1 className="display-4 text-white mt-5 mb-2">
              {title}
            </h1>
            <h2 className="mb-5 text-white ">{headline}</h2>
            {children}
          </Col>
        </Row>
      </Container>

    </header>
  )
}

Header.defaultProps = {
  height: "100%",
  image: "https://images.unsplash.com/photo-1630011725376-bd68a6403318?ixid=MnwxMjA3fDB8MHx0b3BpYy1mZWVkfDN8Ym84alFLVGFFMFl8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
}

export default Header