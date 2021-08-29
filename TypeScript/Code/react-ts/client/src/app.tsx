import React from "react"
import { Switch, Route } from "react-router"
import routes from "./config/routes"

export interface IApplicationsProps { }

const Application: React.FunctionComponent<IApplicationsProps> = props => {
    return (
        <Switch>
            {routes.map((route, index) => {
                return (
                    <Route
                        key={index}
                        exact={route}
                    >

                    </Route>
                )
            })}
        </Switch>
    )
}

export default Application