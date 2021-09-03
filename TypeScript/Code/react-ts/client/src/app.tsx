import React from "react"
import { Switch, Route, RouteChildrenProps } from "react-router"
import routes from "./config/routes"

export interface IApplicationsProps { }

const Application: React.FunctionComponent<IApplicationsProps> = props => {
    return (
        <Switch>
            {routes.map((route, index) => {
                return (
                    <Route
                        key={index}
                        exact={route.exact}
                        path={route.path}
                        render={(routeProps: RouteChildrenProps<any>) => <route.component {...routeProps} />}
                    >

                    </Route>
                )
            })}
        </Switch>
    )
}

export default Application