import React from "react"
import { Container } from "reactstrap"
import Navigation from "../components"
import Header from "../components/Header"
import IPageProps from "../interface/pages"

const HomePage: React.FunctionComponent<IPageProps> = props => {
    return (
        <Container fluid className="p-0">
            <Navigation>
                <Header title="A nerby Blog "
                    headline="Check out what people shay to say"
                />
                <Container className="mt-5">
                    Blog herre
                </Container>
            </Navigation>
        </Container>
    )
}
export default HomePage