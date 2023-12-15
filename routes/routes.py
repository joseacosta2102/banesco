from fastapi import APIRouter
import routes.auth_c2p as auth_c2p_routes
import routes.register_c2p as register_c2p_routes
import routes.pay_c2p as pay_c2p_routes

router = APIRouter()

router.include_router(auth_c2p_routes.router)
router.include_router(register_c2p_routes.router)
router.include_router(pay_c2p_routes.router)
