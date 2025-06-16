from fastapi import HTTPException, status

def producto_no_encontrado_exception():
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Producto no encontrado"
    )

def producto_existente_exception():
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Ya existe un producto con ese nombre"
    )

def error_crear_producto_exception():
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Error al intentar crear el producto"
    )

def error_eliminar_producto_exception():
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Error al intentar eliminar el producto"
    )
