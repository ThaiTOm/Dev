import React from "react"
import { Link } from "react-router-dom"
import { Container, Nav, Navbar, NavbarBrand } from "reactstrap"
export interface InavigationProps { }

const Navigation: React.FunctionComponent<InavigationProps> = props => {
  return (
    <Navbar color="light" light sticky="top" expand="md">
      <Container>
        <NavbarBrand tag={Link} to="/">Go Back</NavbarBrand>
        <Nav className="mr_auto" navbar />

      </Container>
    </Navbar>
  )
}

export default Navigation