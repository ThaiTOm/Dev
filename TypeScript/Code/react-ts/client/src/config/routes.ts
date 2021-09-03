import IRoute from "../interface/routes";
import LoginPage from "../pages/login"
import BlogPage from "../pages/blog"
import EditPage from "../pages/edit"
import MainPage from "../pages/homePages"
import HomePage from "../pages/homePages";

const authRoutes: IRoute[] = [
    {
        path: "/login",
        exact: true,
        auth: false,
        component: LoginPage,
        name: "Login"
    },
    {
        path: "/register",
        exact: true,
        auth: false,
        component: LoginPage,
        name: "Register"
    }
]

const blogRoutes: IRoute[] = [
    {
        path: "/edit",
        exact: true,
        auth: false,
        component: EditPage,
        name: "Edit"
    },
    {
        path: "/edit/:blogID",
        exact: true,
        auth: true,
        component: BlogPage,
        name: "Blog"
    },
    {
        path: "/blogs/:blogID",
        exact: true,
        auth: false,
        component: BlogPage,
        name: "Login"
    }
]

const mainRoutes: IRoute[] = [
    {
        path: "/home",
        exact: true,
        auth: false,
        component: HomePage,
        name: "Home"
    }
]

const routes: IRoute[] = [
    ...authRoutes,
    ...blogRoutes,
    ...mainRoutes
]
export default routes