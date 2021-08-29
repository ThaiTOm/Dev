import IRoute from "../interface/routes";

const authRoutes: IRoute[] = []

const blogRoutes: IRoute[] = []

const mainRoutes: IRoute[] = []

const routes: IRoute[] = [
    ...authRoutes,
    ...blogRoutes,
    ...mainRoutes
]
export default routes