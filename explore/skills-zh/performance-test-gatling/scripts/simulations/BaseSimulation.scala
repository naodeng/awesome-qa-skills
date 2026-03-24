package simulations

import io.gatling.core.Predef._
import io.gatling.http.Predef._

import scala.concurrent.duration._

abstract class BaseSimulation extends Simulation {
  val baseUrl: String = sys.env.getOrElse("BASE_URL", "https://test.k6.io")
  val envName: String = sys.env.getOrElse("ENV", "staging")

  val httpProtocol = http
    .baseUrl(baseUrl)
    .acceptHeader("application/json, text/html")
    .contentTypeHeader("application/json")
    .userAgentHeader("gatling-performance-test")

  def defaultPause: PauseBuilder = pause(500.millis, 1500.millis)

  def homepageChain(testType: String) = exec(
    http(s"$testType-homepage")
      .get("/")
      .check(status.in(200, 201, 204))
  ).exec(defaultPause)

  def apiProbeChain(testType: String) = exec(
    http(s"$testType-api-probe")
      .get("/")
      .check(status.in(200, 201, 204))
  ).exec(defaultPause)
}
