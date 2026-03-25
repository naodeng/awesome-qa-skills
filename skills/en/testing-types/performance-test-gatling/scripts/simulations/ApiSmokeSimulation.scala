package simulations

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class ApiSmokeSimulation extends BaseSimulation {

  private val feeder = Iterator.continually(
    Map(
      "skuId" -> s"SKU-${1000 + util.Random.nextInt(100)}",
      "userTier" -> (if (util.Random.nextBoolean()) "PLUS" else "NORMAL")
    )
  )

  private val apiScenario = scenario(s"api-smoke-$envName")
    .feed(feeder)
    .forever {
      apiProbeChain("smoke")
        .exec(
          http("smoke-api-login")
            .post("/api/login/")
            .body(StringBody("""{"skuId":"${skuId}","userTier":"${userTier}"}""")).asJson
            .check(status.in(200, 201, 204))
            .check(responseTimeInMillis.lte(1000))
        )
        .pause(200.millis, 600.millis)
    }

  setUp(
    apiScenario.injectOpen(
      constantUsersPerSec(10).during(3.minutes)
    )
  ).protocols(httpProtocol)
    .assertions(
      global.failedRequests.percent.lt(1.0),
      global.responseTime.percentile3.lt(1000),
      global.responseTime.percentile4.lt(1800)
    )
}
