# Build stage
FROM adoptopenjdk/openjdk11:jdk-11.0.11_9-alpine AS build
COPY /totalhrs /app
WORKDIR /app
RUN ./mvnw package -DskipTests

# Runtime stage
FROM adoptopenjdk/openjdk11:jre-11.0.11_9-alpine
COPY --from=build /app/target/totalhrs-0.0.1-SNAPSHOT.jar /totalhrs.jar
EXPOSE 1030 80

CMD ["java", "-jar", "/totalhrs.jar"]
