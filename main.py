import api
import documentation
import justpy as jp

jp.Route("/", documentation.Documentation.serve)
jp.Route("/api", api.Api.serve)
jp.justpy()