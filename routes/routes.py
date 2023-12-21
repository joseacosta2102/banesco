from fastapi import APIRouter

import routes.auth_c2p as auth_c2p_routes

import routes.confirm_c2p as confirm_c2p_routes
import routes.pay_c2p as pay_c2p_routes
import routes.banks as bank_router

router = APIRouter()

router.include_router(auth_c2p_routes.router)
router.include_router(confirm_c2p_routes.router)
router.include_router(pay_c2p_routes.router)
router.include_router(bank_router.router)
