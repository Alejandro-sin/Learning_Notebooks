
const resolveRoutes = (route) =>{
    if (route.length <=3 ){
        let valdiRoute = route === '/' ? route: '/:id'
        return valdiRoute;
    }
    return `/${route}`;

};

export default resolveRoutes;
