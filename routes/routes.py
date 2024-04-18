from fastapi import APIRouter

import routes.pay_c2p as pay_c2p_routes
import routes.confirm as confirm_routes

router = APIRouter()

router.include_router(pay_c2p_routes.router)
router.include_router(confirm_routes.router)
